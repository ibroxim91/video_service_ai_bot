import json


def main():
    with open("videos.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open("output.sql", "w", encoding="utf-8") as out:
        for v in data['videos']:
            out.write(f"""INSERT INTO videos (id, creator_id, video_created_at, views_count, likes_count,
             comments_count, reports_count, created_at, updated_at) 
                    VALUES ('{v["id"]}','{v["creator_id"]}','{v["video_created_at"]}',{v["views_count"]},
                    {v["likes_count"]},{v["comments_count"]},{v["reports_count"]},'{v["created_at"]}',
                    '{v["updated_at"]}');\n""")


if __name__ == "__main__":
    main()
