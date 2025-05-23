from flask import Flask, request, jsonify
import asyncio

app = Flask(__name__)
bot = None  # This will be set from main.py

@app.route("/verify", methods=["POST"])
def verify():
    global bot
    if bot is None:
        return jsonify({"status": "failure", "reason": "Bot not initialized"}), 500

    data = request.get_json()
    code = data.get("code")
    roblox_name = data.get("roblox_name")

    user_id = bot.verification_cog.check_code(code)
    if not user_id:
        return jsonify({"status": "failure", "reason": "Invalid code"}), 400

    guild = bot.guilds[0] if bot.guilds else None
    if not guild:
        return jsonify({"status": "failure", "reason": "Bot not in any guild"}), 500

    member = guild.get_member(user_id)
    if not member:
        return jsonify({"status": "failure", "reason": "User not in server"}), 404

    try:
        future = asyncio.run_coroutine_threadsafe(member.edit(nick=roblox_name), bot.loop)
        future.result(timeout=10)
        return jsonify({"status": "success", "user_id": user_id})
    except Exception as e:
        return jsonify({"status": "failure", "reason": str(e)}), 500

def run_flask(discord_bot):
    global bot
    bot = discord_bot
    app.run(port=5000, debug=False, use_reloader=False)
