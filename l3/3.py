from gym_duckietown.tasks.task_solution import TaskSolution
import numpy as np
import cv2

class DontCrushDuckieTaskSolution(TaskSolution):
    def __init__(self, generated_task):
        super().__init__(generated_task)

    def solve(self):
        env = self.generated_task['env']
        # getting the initial picture
        obs, _, _, _ = env.step([0,0])
        # convect in for work with cv
        img = cv2.cvtColor(np.ascontiguousarray(obs), cv2.COLOR_BGR2RGB)
        
        # add here some image processing
        lower_yellow = np.array([150,150,0])
        upper_yellow = np.array([255,255,0])

        condition = True
        while condition:
            obs, reward, done, info = env.step([1, 0])
            img = cv2.cvtColor(np.ascontiguousarray(obs), cv2.COLOR_BGR2RGB)

            mask = cv2.inRange(img, lower_yellow, upper_yellow)
            non_zero = np.sum(mask)/255
            total_px = mask.shape[0] * mask.shape[1]
            buf = non_zero/total_px

            if buf > 0.05:
                obs, reward, done, info = env.step([0, 0])
                condition = False

            env.render()
