from gym.envs.registration import register

for v in ['1']:
    register(id='PlaygroundNavigation-v' + v,
             entry_point='playground.playgroundnavv' + v + ':PlayGroundNavigationV' + v,
             max_episode_steps=50)

    register(id='PlaygroundNavigationHuman-v' + v,
             entry_point='playground.playgroundnavv' + v + ':PlayGroundNavigationV' + v,
             max_episode_steps=50,
             kwargs=dict(human=True, render_mode=True))

    register(id='PlaygroundNavigationRender-v' + v,
             entry_point='playground.playgroundnavv' + v + ':PlayGroundNavigationV' + v,
             max_episode_steps=50,
             kwargs=dict(human=False, render_mode=True))
