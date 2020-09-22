%global v2ray_path %{_bindir}/v2ray
%global grant_cap(p) %{expand:
    echo   '  Granting capabilities to %1'
    setcap 'cap_net_bind_service=+ep cap_net_admin=+ep' %1
}
%global revoke_cap(p) %{expand:
    echo   '  Revoking capabilities from %1'
    setcap 'cap_net_bind_service=-ep cap_net_admin=-ep' %1
}

Name:           v2ray-cap
Version:        1.0.1
Release:        1%{?dist}
Summary:        A script for grant network capabilities to %{v2ray_path}

License:        MIT
URL:            https://www.v2fly.org/

Requires:       libcap

BuildArch:      noarch

%description
Installing this package will grant V2Ray core binary the capabilities for transparent proxies.

%prep

%build

%install

# Scriptlets Start
%filetriggerin -- %{v2ray_path}
%grant_cap -p %{v2ray_path}

%preun
%revoke_cap -p %{v2ray_path}

%posttrans
%grant_cap -p %{v2ray_path}
# Scriptlets End

%files

%changelog
* Tue Sep 22 2020 sixg0000d <sixg0000d@gmail.com> - 1.0.0 - 1
- Inital v2ray-cap
* Tue Sep 22 2020 sixg0000d <sixg0000d@gmail.com> - 1.0.1 - 1
- Remove build arch
