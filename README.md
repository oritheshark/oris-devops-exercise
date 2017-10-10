# oris-devops-exercise

Hi there,

In this exercise I used Python/Flask for img-panda service, and node.js for smart-panda service. 
Also, MongoDB (mLab hosted) is used in both of them, for handling the GET counter.
Both of the Ansible roles are also installing Upstart services, so they reload on crash or reboot.

So, what is included:
1. [img-panda](https://github.com/oritheshark/oris-devops-exercise/blob/master/roles/imgpanda/files/imgpanda-app/img-panda.py) and its [Ansible role](https://github.com/oritheshark/oris-devops-exercise/blob/master/roles/imgpanda/tasks/main.yml) - will run on http://localhost:8081/img-panda
2. [smart-panda](https://github.com/oritheshark/oris-devops-exercise/blob/master/roles/smartpanda/files/smartpanda-app/smartpanda.js) and its [Ansible role](https://github.com/oritheshark/oris-devops-exercise/blob/master/roles/smartpanda/tasks/main.yml) - will run on http://localhost:8082/smart-panda
3. Modified [base.yml](https://github.com/oritheshark/oris-devops-exercise/blob/master/base.yml) which includes the required dependencies
4. And the **BONUS** [wrapper script](https://github.com/oritheshark/oris-devops-exercise/blob/master/wrapper.py) to pull latest version and deploy everything from a single line!

I hope you'll enjoy it, waiting for more!
Ori