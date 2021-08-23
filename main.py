import model.envirorment as envirorment

print("**Multiagent Traffic System Simulator**")
print("Team No.6")
# Parameters
parameters = {
    "size" : 20,
    "number_of_agents" : 10,
}
env = envirorment.Env(parameters)
env.setup()
# Main loop
    