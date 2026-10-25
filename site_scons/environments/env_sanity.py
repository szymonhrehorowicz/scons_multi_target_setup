from scons_hints import *

env_sanity = Environment(
    tools=[
        "sanity_tool",
    ],
)

Export("env_sanity")
Return("env_sanity")
