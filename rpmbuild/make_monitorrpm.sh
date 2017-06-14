#!/bin/bash
NAME='factory_monitor'
VERSION=${1:-0.1}
RELEASE=${2:-1}

ROOT_DIR="$(dirname $0)/.."

TMP_DIR=${NAME}-${VERSION}

mkdir -p $TMP_DIR
cp $ROOT_DIR/factory-monitor $TMP_DIR
cp $ROOT_DIR/factory-monitord $TMP_DIR
cp $ROOT_DIR/monitor.py $TMP_DIR
cp $ROOT_DIR/config.json $TMP_DIR
cp $ROOT_DIR/metrics.py $TMP_DIR
cp factory_monitor.spec $TMP_DIR

tar -czvf ${NAME}-${VERSION}.tgz ${NAME}-${VERSION}/

mkdir -p RPMBUILD/{RPMS/noarch,SPECS,BUILD,SOURCES,SRPMS}
rpmbuild --define "_topdir `pwd`/RPMBUILD" \
         --define "ver ${VERSION}"         \
         --define "rel ${RELEASE}"         \
         --define "name ${NAME}"           \
         -tb ./${NAME}-${VERSION}.tgz

find RPMBUILD/ -type f -name "*.rpm" -exec mv {} . \;
rm -rf RPMBUILD/ ${NAME}-${VERSION}/ ./${NAME}-${VERSION}.tgz
