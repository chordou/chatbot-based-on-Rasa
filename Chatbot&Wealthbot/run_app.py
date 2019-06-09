from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig


nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
action_endpoint = EndpointConfig(url="http://localhost:5005/webhooks/slack/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('xoxb-626938457776-620596434449-iaW4Ef00VtIM5oYEl7BWiHmK' #your bot user authentication token
                           )

agent.handle_channels([input_channel], 5005, serve_forever=True)