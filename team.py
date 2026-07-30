from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

eng_agent = Agent(name="English Agent" , role="You answer questions in English")
chi_agent = Agent(name="Chinese Agent" , role="You answer questions in Chinese")
thai_agent = Agent(name="Thai Agent" , role="You answer questions in Thai")
hindi_agent = Agent(name="Hindi Agent" , role="You answer questions in Hindi")

team_leader = Team(
    name = "Answer & Translation Team",
    members=[eng_agent , chi_agent , thai_agent , hindi_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    show_members_responses=True,
    instructions ="""All member agents must respond to answer the query in their speceific language.
                     Do not route to just one agent.
                     Output the response of all agents
      """,
    
)


team_leader.print_response("What is the capital of India")


# there is agent which have the model and tools now let learn about the memory