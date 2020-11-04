# ROS

## 1 лабораторная
Чтобы запустить, воспользуйтесь скриптом `run_lab1.sh`.

### Задание
- Разработать ноду, которая позволит одной черепашке (пакет turtlesim, нода turtlesim_node) двигаться за другой такой же, но управляемой с клавиатуры.  
- Запуск всех нод должен осуществляться из одного launch файла.  

### Ноды
* leonardo - turtlesim_node  
* turtle_teleop_key - нода для управления первой черепахой turtle_1 при помощи клавиатуры  
* spawner (spawner.py) - нода для создания второй черепахи turtle_2  
* main (main.py) - нода для того, чтобы вторая черепаха turtle_2 двигалась за первой turtle_1  
  Создан подписчик sub1. Если первая черепаха начинает движение (изменяет свое положение), то sub1 вызывает функцию follow для расчета вектора движения второй черепахи. Подписчик sub2 хранит текущее положение второй черепахи. А затем результат передается в топик второй черепахи.  

