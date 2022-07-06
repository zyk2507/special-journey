## iperf3

```bash
iperf3 -c [server addr] -p [port number]
```

### installing

```bash
sudo adduser iperf --disabled-login --gecos iperf

sudo nano /etc/systemd/system/iperf3-server@.service
```

edit with following contents

```systemd
[Unit]
Description=iperf3 server on port %i
After=syslog.target network.target

[Service]
ExecStart=/usr/bin/iperf3 -s -1 -p %i
Restart=always
RuntimeMaxSec=3600
User=iperf

[Install]
WantedBy=multi-user.target
DefaultInstance=5201
```

```bash
sudo systemctl daemon-reload


for p in $(seq 9200 9220); do sudo systemctl enable --now iperf3-server@$p ; done
```

to disable

```bash
for p in $(seq 9200 9220); do sudo systemctl disable iperf3-server@$p ; done
```

---

#### Run multiple threads

```bash
iperf -c [server addr] -p [port number] -P [thread num]
```

#### Change the test duration(server side)

```bash
iperf -s -t 60
```


