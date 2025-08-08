import os
import requests
from flask_restx import Namespace, Resource
from flask import request

unsplash_ns = Namespace("unsplash", description="Unsplash image proxy")

UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")


@unsplash_ns.route("/photo")
class UnsplashPhoto(Resource):
    def get(self):
        """Proxy to fetch a random Unsplash photo by query"""

        if not UNSPLASH_ACCESS_KEY:
            return {"error": "Unsplash API key not set"}, 500
        query = request.args.get("query", "house")
        url = "https://api.unsplash.com/photos/random"
        params = {"query": query, "client_id": UNSPLASH_ACCESS_KEY}
        resp = requests.get(url, params=params)
        if resp.ok:
            data = resp.json()
            return {
                "url": data["urls"]["regular"],
                "credit": data["user"]["name"],
                "profile": data["user"]["links"]["html"],
            }
        else:
            return {"error": "Failed to fetch Unsplash image"}, 500
