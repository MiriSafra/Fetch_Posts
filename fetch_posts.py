import argparse
import json

import requests
import os


# response = requests.get("https://jsonplaceholder.typicode.com/posts")
def fetch_posts(api_url, userId=None):
    params = {}
    if userId:
        params["userId"] = userId
    response = requests.get(api_url, params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching data from API")


def filter_posts(posts, include_body=False):
    filtered = []
    for post in posts:
        if include_body:
            filtered.append({
                "title": post["title"],
                "body": post["body"]
            })
        else:
            filtered.append({
                "title": post["title"]
            })
    return filtered


def main():
    parser = argparse.ArgumentParser(description="show posts per usrId")

    parser.add_argument("--api", type=str, required=True, help="api url")
    parser.add_argument("--userId", type=int, required=False, help="user id")
    parser.add_argument("--output", type=str, required=False, help="file output")
    parser.add_argument("--include_body", action="store_true", required=False, help="include body")

    args = parser.parse_args()
    posts = fetch_posts(args.api, args.userId)
    filtered = filter_posts(posts, args.include_body)
    format = ""
    if args.output:
        _, ext = os.path.splitext(args.output)
        if ext == ".json":
            format = "json"
        elif ext == ".txt":
            format = "txt"
        if format != "txt" and format != "json":
                print(f"Unsupported file extension: {ext}")
                exit(1)
        with open(args.output, "w", encoding="utf-8") as f:
            if format == "json":
                json.dump(filtered, f, ensure_ascii=False, indent=2)
            else:
                for post in filtered:
                    f.write(f"**{post['title']}**\n")
                    if args.include_body:
                        f.write(f"{post['body']}\n")
                    f.write("---------------------------\n")

        print(f"\n✅ Saved output to {args.output}")
    else:
        for post in filtered:
            print(post["title"])
            if args.include_body:
                print(post["body"])
            print("---------------------------")


if __name__ == "__main__":
    main()