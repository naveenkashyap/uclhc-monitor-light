%{!?ver:          %define ver      0.1}
%{!?rel:          %define rel      1}
%{!?name:         %define name      factory_monitor}

Name:           %{name}
Version:        %{ver}
Release:        %{rel}
Summary: Visualizes Condor Factory meta data in Grafana

Requires: influxdb grafana-server

%description
This python-based program uses bindings to the Condor Batch system to store data into
influxdb, which is then read and visualized by a Grafana server

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/var/lib/factory-monitor
mkdir -p %{buildroot}/var/lib/factory-monitor/outboxes
mkdir -p %{buildroot}/var/cache/factory-monitor
mkdir -p %{buildroot}/var/log/factory-monitor

install -m 777 factory-monitor %{buildroot}/etc/init.d
install -m 777  factory-monitord %{buildroot}/usr/sbin
install -m 777 monitor.py %{buildroot}/var/lib/factory-monitor
install -m 777 config.json %{buildroot}/var/lib/factory-monitor
install -m 777 metrics.py %{buildroot}/var/lib/factory-monitor

%clean
rm -rf %{buildroot}
