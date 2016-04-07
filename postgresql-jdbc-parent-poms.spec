# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global section		devel
%global archive_name    pgjdbc-parent-poms
Summary:	Parent poms for jdbc project
Name:		postgresql-jdbc-parent-poms
Version:	1.0.3
Release:	1%{?dist}
License:	BSD
Group:		Applications/Databases
URL:		https://github.com/pgjdbc/pgjdbc-parent-poms/

Source0:	https://github.com/pgjdbc/pgjdbc-parent-poms/archive/REL%{version}.tar.gz
Patch1:		standard_directory.patch

BuildArch:	noarch
BuildRequires:	java-devel >= 1:1.8
BuildRequires:	jpackage-utils
BuildRequires:	maven-local
BuildRequires: os-maven-plugin
Requires:	jpackage-utils
Requires:	java-headless >= 1:1.8

%description
This package includes maven parent poms that are used by PostgreSQL JDBC driver.

%prep
%setup -c -q
mv -f %{archive_name}-REL%{version}/* .
%patch1 -p1

# remove any binary libs
find -name "*.jar" -or -name "*.class" | xargs rm -f

%pom_remove_dep com.github.dblock.waffle:waffle-jna pgjdbc-core-parent/pom.xml 
%pom_remove_dep org.osgi:org.osgi.enterprise pgjdbc-core-parent/pom.xml

%build
%mvn_build -f

%install
%mvn_install

%check

%files -f .mfiles 

%changelog
* Tue Jan 5 2016 Pavel Kajaba <pkajaba@redhat.com>
- Initial creation of postgresql-jdbc-parent-poms package
