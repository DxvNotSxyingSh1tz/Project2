from flask import Flask, request, jsonify
import asyncio
import os

app = Flask(__name__)
bot = None  # Will be injected by main.py


@app.route("/verify", methods=["POST"])
def verify():
    global bot

    if bot is None:
        app.logger.error("❌ Discord bot not initialized.")
        return jsonify({"status": "failure", "reason": "Bot not initialized"}), 500

    data = request.get_json()
    if not data:
        return jsonify({"status": "failure", "reason": "No data received"}), 400

    code = data.get("code")
    roblox_name = data.get("roblox_name")

    if not code or not roblox_name:
        return jsonify({"status": "failure", "reason": "Missing code or roblox_name"}), 400

    user_id = bot.verification_cog.check_code(code)
    if not user_id:
        return jsonify({"status": "failure", "reason": "Invalid or expired code"}), 400

    guild = bot.guilds[0] if bot.guilds else None
    if not guild:
        return jsonify({"status": "failure", "reason": "Bot is not in any guild"}), 500

    member = guild.get_member(user_id)
    if not member:
        return jsonify({"status": "failure", "reason": "User not found in the guild"}), 404

    try:
        future = asyncio.run_coroutine_threadsafe(member.edit(nick=roblox_name), bot.loop)
        future.result(timeout=10)
        return jsonify({"status": "success", "user_id": user_id})
    except Exception as e:
        app.logger.error(f"Failed to set nickname: {e}")
        return jsonify({"status": "failure", "reason": str(e)}), 500


def run_flask(discord_bot):
    global bot
    bot = discord_bot
    port = int(os.environ.get("PORT", 5000))
    app.logger.info(f"✅ Flask app starting on 0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port)


