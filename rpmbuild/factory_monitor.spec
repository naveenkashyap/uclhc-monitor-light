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

