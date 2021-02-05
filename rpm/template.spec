%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-laser-geometry
Version:        1.6.7
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS laser_geometry package

License:        BSD
URL:            http://ros.org/wiki/laser_geometry
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       eigen3-devel
Requires:       python3-numpy
Requires:       ros-noetic-angles
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf2
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-noetic-angles
BuildRequires:  ros-noetic-catkin >= 0.5.68
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rosunit
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf2
BuildRequires:  ros-noetic-tf2-geometry-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This package contains a class for converting from a 2D laser scan as defined by
sensor_msgs/LaserScan into a point cloud as defined by sensor_msgs/PointCloud or
sensor_msgs/PointCloud2. In particular, it contains functionality to account for
the skew resulting from moving robots or tilting laser scanners.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Feb 05 2021 Dave Hershberger <dave.hershberger@sri.com> - 1.6.7-1
- Autogenerated by Bloom

* Thu Jan 14 2021 Dave Hershberger <dave.hershberger@sri.com> - 1.6.6-1
- Autogenerated by Bloom

* Fri Mar 13 2020 Dave Hershberger <dave.hershberger@sri.com> - 1.6.5-1
- Autogenerated by Bloom

