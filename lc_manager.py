import argparse
import sqlite3
from datetime import datetime
import os

DB_NAME="leetcode.db"

def init_db():
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS solutions (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT NOT NULL,
     difficulty TEXT NOT NULL,
     topic TEXT NOT NULL,
     date_added TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def add_solution_to_db(name,difficulty,topic):
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()

    date_now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
    INSERT INTO solutions (name, difficulty, topic, date_added)
    VALUES (?, ?, ?, ?)
    ''',(name, difficulty, topic, date_now))

    conn.commit()
    conn.close()
    print(f"Saved '{name}' into database.")

def create_structure(name,topic):
    folder_name=name.lower().replace(" ","_").replace("-","_")
    topic_folder=topic.lower().replace(" ","_").replace("-","_")

    path=os.path.join(topic_folder,folder_name)

    os.makedirs(path, exist_ok=True)

    solution_code= """class Solution:
    def solve(self):
        pass
    """

    test_code="""import pytest
from solution import Solution
    
def test_solve():
sol=Solution()
# TODO: write assertion
assert sol.solve()==None
    """
    with open(os.path.join(path,"solution.py"),"w",encoding="utf-8") as f:
        f.write(solution_code)
    with open(os.path.join(path,"test_solution.py"),"w",encoding="utf-8") as f:
        f.write(test_code)

    print(f"Created files in {path}")

def generate_readme():
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    cursor.execute("Select id, name, difficulty, topic, date_added FROM solutions ORDER BY id")
    rows=cursor.fetchall()
    conn.close()
    md_content = "LeetCode Tracker\n\n"
    md_content += "A personal repository containing my solutions to various algorithmic problems. "
    md_content += "This entire workspace, including the table below, is generated and maintained automatically via a custom Python CLI tool.\n\n"

    md_content += "| ID | Problem | Topic | Difficulty | Date Solved |\n"
    md_content += "|---|---|---|---|---|\n"

    for row in rows:
        task_id, name, difficulty, topic, date_added = row

        folder_name=name.lower().replace(" ","_").replace("-","_")
        topic_folder=topic.lower().replace(" ","_").replace("-","_")
        path=f"./{topic_folder}/{folder_name}/solution.py"

        md_content += f"| {task_id} | [{name}]({path}) | {topic} | {difficulty} | {date_added} |\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(md_content)

    print(" README.md has been generated.")
def main():
    init_db()
    parser=argparse.ArgumentParser()
    subparsers=parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("name",type=str)
    add_parser.add_argument("--difficulty",choices=["easy","medium","hard"],required=True)
    add_parser.add_argument("--topic",type=str,required=True)

    readme_parser = subparsers.add_parser("generate-readme")

    args=parser.parse_args()

    if args.command == "add":
        print("--- New Task Received --")
        print(f"Name: {args.name}")
        print(f"Difficulty: {args.difficulty}")
        print(f"Topic: {args.topic}")

        add_solution_to_db(args.name,args.difficulty,args.topic)

        create_structure(args.name,args.topic)
    elif args.command == "generate-readme":
        generate_readme()
if __name__ == "__main__":
    main()