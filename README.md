[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20384607&assignment_repo_type=AssignmentRepo)

# MiniTorch Module 1

<img src="https://minitorch.github.io/minitorch.svg" width="50%">

* Docs: https://minitorch.github.io/

* Overview: https://minitorch.github.io/module1/module1/

This assignment requires the following files from the previous assignments. You can get these by running

```bash
python sync_previous_module.py previous-module-dir current-module-dir
```

The files that will be synced are:

        minitorch/operators.py minitorch/module.py tests/test_module.py tests/test_operators.py project/run_manual.py

## Task 1.5

### Dataset: Simple

- Number of points: 50
- Size of hidden layer: 2
- Learning rate: 0.5
- Number of epochs: 100

*Logs*:
<br>
Epoch: 10/100, loss: 33.15358766474338, correct: 36
<br>
Epoch: 20/100, loss: 28.899587592884128, correct: 41
<br>
Epoch: 30/100, loss: 20.560705800069513, correct: 47
<br>
Epoch: 40/100, loss: 13.06124333196778, correct: 50
<br>
Epoch: 50/100, loss: 9.264615932182334, correct: 49
<br>
Epoch: 60/100, loss: 7.190629279279249, correct: 49
<br>
Epoch: 70/100, loss: 5.883098757186656, correct: 50
<br>
Epoch: 80/100, loss: 5.025889754206336, correct: 50
<br>
Epoch: 90/100, loss: 4.386044239437491, correct: 50
<br>
Epoch: 100/100, loss: 3.8896420504992513, correct: 50

*Final image*:
<br>
<img src="https://github.com/minitorch/minitorch-module-1-GrishHelen/blob/master/img/Simple_trained.png" width="300">

### Dataset: Diag

- Number of points: 50
- Size of hidden layer: 3
- Learning rate: 0.5
- Number of epochs: 100

*Logs*:
<br>
Epoch: 10/100, loss: 11.781105299873317, correct: 46
<br>
Epoch: 20/100, loss: 10.9011292005061, correct: 46
<br>
Epoch: 30/100, loss: 9.844545222451753, correct: 46
<br>
Epoch: 40/100, loss: 8.553937971032914, correct: 46
<br>
Epoch: 50/100, loss: 7.239970353357007, correct: 46
<br>
Epoch: 60/100, loss: 6.231692153070737, correct: 46
<br>
Epoch: 70/100, loss: 5.320612236382831, correct: 46
<br>
Epoch: 80/100, loss: 4.54409909710117, correct: 48
<br>
Epoch: 90/100, loss: 3.9251390034255533, correct: 49
<br>
Epoch: 100/100, loss: 3.4987644691809012, correct: 49

*Final image*:
<br>
<img src="https://github.com/minitorch/minitorch-module-1-GrishHelen/blob/master/img/Diag_trained.png" width="300">

### Dataset: Split

- Number of points: 50
- Size of hidden layer: 10
- Learning rate: 0.5
- Number of epochs: 200

*Logs*:
<br>
Epoch: 10/200, loss: 33.4548728575794, correct: 31
<br>
Epoch: 20/200, loss: 32.205898818361895, correct: 30
<br>
Epoch: 30/200, loss: 31.13372179572381, correct: 34
<br>
Epoch: 40/200, loss: 29.940163043773165, correct: 35
<br>
Epoch: 50/200, loss: 28.37784454048394, correct: 35
<br>
Epoch: 60/200, loss: 26.39987228025115, correct: 40
<br>
Epoch: 70/200, loss: 24.010847622366345, correct: 41
<br>
Epoch: 80/200, loss: 31.859492503659546, correct: 31
<br>
Epoch: 90/200, loss: 26.47186169056214, correct: 33
<br>
Epoch: 100/200, loss: 21.085377727772055, correct: 38
<br>
Epoch: 110/200, loss: 21.172357974968534, correct: 40
<br>
Epoch: 120/200, loss: 21.31450154608139, correct: 38
<br>
Epoch: 130/200, loss: 18.11008998928775, correct: 42
<br>
Epoch: 140/200, loss: 13.858470166773817, correct: 44
<br>
Epoch: 150/200, loss: 9.737520345245256, correct: 46
<br>
Epoch: 160/200, loss: 8.412503186203544, correct: 48
<br>
Epoch: 170/200, loss: 8.09017362813796, correct: 46
<br>
Epoch: 180/200, loss: 46.117409217046614, correct: 30
<br>
Epoch: 190/200, loss: 8.034029338943535, correct: 48
<br>
Epoch: 200/200, loss: 6.75629967679229, correct: 48

*Final image*:
<br>
<img src="https://github.com/minitorch/minitorch-module-1-GrishHelen/blob/master/img/Split_trained.png" width="300">

### Dataset: XOR

- Number of points: 100
- Size of hidden layer: 7
- Learning rate: 0.5
- Number of epochs: 200

*Logs*:
<br>
Epoch: 10/200, loss: 66.74370273913931, correct: 65
<br>
Epoch: 20/200, loss: 63.86339089597266, correct: 70
<br>
Epoch: 30/200, loss: 62.57334818744039, correct: 58
<br>
Epoch: 40/200, loss: 63.8933994488674, correct: 54
<br>
Epoch: 50/200, loss: 55.39901696766182, correct: 71
<br>
Epoch: 60/200, loss: 53.14911064835187, correct: 70
<br>
Epoch: 70/200, loss: 42.60406087752197, correct: 76
<br>
Epoch: 80/200, loss: 40.60449166564564, correct: 84
<br>
Epoch: 90/200, loss: 33.42976119909457, correct: 86
<br>
Epoch: 100/200, loss: 68.5823840265058, correct: 72
<br>
Epoch: 110/200, loss: 28.377820755235803, correct: 88
<br>
Epoch: 120/200, loss: 24.5314664568978, correct: 92
<br>
Epoch: 130/200, loss: 25.786713000332973, correct: 83
<br>
Epoch: 140/200, loss: 41.393799632333526, correct: 76
<br>
Epoch: 150/200, loss: 21.303742451128876, correct: 90
<br>
Epoch: 160/200, loss: 31.124295849462044, correct: 85
<br>
Epoch: 170/200, loss: 35.802788414974735, correct: 83
<br>
Epoch: 180/200, loss: 14.53484123991363, correct: 96
<br>
Epoch: 190/200, loss: 32.89716770118068, correct: 85
<br>
Epoch: 200/200, loss: 15.929003814020806, correct: 96

*Final image*:
<br>
<img src="https://github.com/minitorch/minitorch-module-1-GrishHelen/blob/master/img/XOR_trained.png" width="300">


