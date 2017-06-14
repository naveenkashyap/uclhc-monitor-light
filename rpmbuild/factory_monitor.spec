%{!?ver:          %define ver      0.1}
%{!?rel:          %define rel      1}
%{!?name:         %define name      factory_monitor}

Name:           %{name}
Version:        %{ver}
Release:        %{rel}
Summary: Visualizes Condor Factory meta data in Grafana
License: Apache 2.0

Source0:	%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:  noarch

Requires: python

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
mkdir -p %{buildroot}/etc/init.d
mkdir -p %{buildroot}/usr/sbin

install -m 777 factory-monitor %{buildroot}/etc/init.d
install -m 777  factory-monitord %{buildroot}/usr/sbin
install -m 777 monitor.py %{buildroot}/var/lib/factory-monitor
install -m 777 config.json %{buildroot}/var/lib/factory-monitor
install -m 777 metrics.py %{buildroot}/var/lib/factory-monitor

%postun
if [ "$1" = "0" ] ; then #Remove package
  rm -rf /var/lib/factory-monitor
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/etc/init.d/factory-monitor
/usr/sbin/factory-monitord
%config(noreplace) /var/lib/factory-monitor/config.json
%config(noreplace) /var/lib/factory-monitor/metrics.py*
/var/lib/factory-monitor/monitor.py*