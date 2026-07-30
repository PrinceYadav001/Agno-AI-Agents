from agno.agent import Agent 
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

load_dotenv()

# there is two type of Memory 1) short term 2)long Term

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Groq(id="llama-3.3-70b-versatile"),
        markdown="True",
        add_history_to_context=True,
        enable_user_memories=True
    )

agent = build_agent()

user_id ="princeyadav@gmail.com"
agent.print_response("What is the captial of Austrailli?" , user_id=user_id)
agent.print_response("What is the best time to visit it?" ,user_id=user_id)

memories= agent.get_user_memories(
    user_id=user_id
)

print("MEMORIES: ")
pprint(memories)