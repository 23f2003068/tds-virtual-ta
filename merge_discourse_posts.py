import os
import json

INPUT_DIR = "tds_pages_json"
OUTPUT_FILE = "discourse_posts.json"

all_posts = []

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".json"):
        filepath = os.path.join(INPUT_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            topic_data = json.load(f)
            topic_id = topic_data.get("topic_id")
            topic_title = topic_data.get("title", "")
            for post in topic_data.get("posts", []):
                post_entry = {
                    "topic_id": topic_id,
                    "topic_title": topic_title,
                    "post_number": post.get("post_id"),
                    "reply_to_post_number": None,  # Optional: fill if your JSON has it
                    "content": post.get("content", "")
                }
                all_posts.append(post_entry)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_posts, f, ensure_ascii=False, indent=2)

print(f"✅ Merged {len(all_posts)} posts into {OUTPUT_FILE}")
