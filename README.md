# gym-chrome-dino

An OpenAI Gym environment for Chrome Dino / T-Rex Runner Game

![screenshot](https://user-images.githubusercontent.com/10172439/54082936-eda8f700-4357-11e9-9b86-662962c334e9.jpg)

This environment utilizes 
[a forked version](https://github.com/elvisyjlin/t-rex-runner) 
of _Chrome Dino_, also called _T-Rex Runner_, 
extracted from chromium offline error page. 
See [here](https://github.com/wayou/t-rex-runner).


## Installation

You can install `gym-chrome-dino` from PyPI by either 

```bash
pip install gym-chrome-dino
```

or

```bash
git clone https://github.com/elvisyjlin/gym-chrome-dino.git
cd gym-chrome-dino
pip install -e .
```


## Usage

You can get started as follows:

```python
import gym
import gym_chrome_dino
env = gym.make('ChromeDino-v0')
```

To create a headless (without opening browser) environment

```python
env = gym.make('ChromeDinoNoBrowser-v0')
```

### Observations, Actions and Rewards

* The observation is a RGB numpy array with shape of (150, 600, 3).  
* The available actions are 0: _do nothing_, 1: _jump_, and 2: _duck_.  
* A positive reward 0.01 is given when the dinosaur is alive; a negative penalty -1.0 is given when the dinosaur hits an obstable, which might be a cactus or a bird.

For the DeepMind DQN recipe, where we give 4-stacked resized grayscaled frames (80, 160, 4) to the agent, we provide a wrapping method `make_dino()`. It also comes with a timer wrapper, which reports the interval between `env.step()`.

```python
from gym_chrome_dino.wrappers import make_dino
env = make_dino(env, timer=True, frame_stack=True)
```

### DinoGame

An instance of `DinoGame` is created when the environment is made. There are some useful methods for fine control of the training environment. The `DineGame` can be accessed as follows:

```python
env.unwrapped.game
```

`DinoGame` provides a `get_score()` method to get the score of current game.

```python
score = env.unwrapped.game.get_score()
```

By default, the acceleration of the game is set to zero. If you want to restore the original acceleration value, please do `set_acceleration(True)`. On the other hand, `set_acceleration(False)` sets the value to zero.

```python
env.unwrapped.game.set_acceleration(True)
```


## Example

Here is a simple example to use `gym-chrome-dino`.

```python
import gym
import gym_chrome_dino
from gym_chrome_dino.utils.wrappers import make_dino
env = gym.make('ChromeDino-v0')
env = make_dino(env, timer=True, frame_stack=True)
done = True
while True:
    if done:
        env.reset()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
```


## WebDriver

`gym-chrome-dino` runs the game on [chromedriver](http://chromedriver.chromium.org) via `selenium` because it is a proper way to monitor and to play _Chrome Dino_. As a result, the latest chromedriver executable file will be downloaded to the current working directory where your program is.
