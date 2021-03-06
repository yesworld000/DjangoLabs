-- SQLite
INSERT INTO main_task (id, task, what_to_do, comments)
VALUES (1, 'task 1', 'to play with kids', 'neighbors kids are annoying');

INSERT INTO main_task (id, task, what_to_do, comments)
VALUES (5, 'task 2', 'to go for a shop', 'to buy potato');

INSERT INTO main_todo (id, created, due_on, owner, mark, task_id)
VALUES (1, '05.03.2021', '08.03.2021', 'admin', 'not done', 1);

INSERT INTO main_todo (id, created, due_on, owner, mark, task_id)
VALUES (2, '03.03.2021', '10.03.2021', 'admin', 'done', 2);