from task_date import TaskDate
from task_recurrent import TaskRecurrent
from task import Task

task_date = TaskDate("Esta es la tarea 1", "14/08/25")
task_recurrent = TaskRecurrent("Esta es la tarea 2", 2)

task_date.mostrar_tarea()
task_recurrent.mostrar_tarea()

