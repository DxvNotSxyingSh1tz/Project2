from flask import Flask, request, jsonify
import asyncio

app = Flask(__name__)

# Global bot variable to be set externally
bot = None

@app.route("/verify", methods=["POST"])
def verify():
    global bot
    if bot is None:
        return jsonify({"status": "failure", "reason": "Bot not initialized"}), 500

    data = request.get_json(force=True)
    code = data.get("code")
    roblox_name = data.get("roblox_name")

    # Example: bot has a sync method to check code, replace with your logic
    user_id = bot.verification_cog.check_code(code) if hasattr(bot, "verification_cog") else None
    if not user_id:
        return jsonify({"status": "failure", "reason": "Invalid code"}), 400

    guild = bot.guilds[0] if bot.guilds else None
    if not guild:
        return jsonify({"status": "failure", "reason": "Bot not in any guild"}), 500

    member = guild.get_member(user_id)
    if not member:
        return jsonify({"status": "failure", "reason": "User not in server"}), 404

    try:
        # Schedule coroutine in bot's event loop thread safely
        future = asyncio.run_coroutine_threadsafe(member.edit(nick=roblox_name), bot.loop)
        future.result(timeout=10)
        return jsonify({"status": "success", "user_id": user_id})
    except Exception as e:
        return jsonify({"status": "failure", "reason": str(e)}), 500


def run_flask():
    # Use waitress (production WSGI server) or gunicorn to serve in prod
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
