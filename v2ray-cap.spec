%global v2ray_path %{_bindir}/v2ray

Name:           v2ray-cap
Version:        1.0.3
Release:        1%{?dist}
Summary:        A script for grant network capabilities to v2ray binary.

License:        MIT
URL:            https://github.com/sixg0000d-copr/copr-v2ray-cap/

Requires:       libcap
Requires:       %{v2ray_path}

BuildArch:      noarch

%description
Installing this package will grant V2Ray core binary the capabilities for transparent proxies.

%prep

%build

%install

# Scriptlets Start
%define grant_cap(p:) %{expand:
    echo   '  Granting capabilities to %{-p*}'
    setcap 'cap_net_bind_service=+ep cap_net_admin=+ep' %{-p*} || :
}

%define revoke_cap(p:) %{expand:
    echo   '  Revoking capabilities from %{-p*}'
    setcap 'cap_net_bind_service=-ep cap_net_admin=-ep' %{-p*} || :
}

%filetriggerin -- %{v2ray_path}
%grant_cap -p %{v2ray_path}

%preun
%revoke_cap -p %{v2ray_path}

%posttrans
%grant_cap -p %{v2ray_path}
# Scriptlets End

%files

%changelog
* Sat Sep 26 2020 sixg0000d <sixg0000d@gmail.com> - 1.0.3 - 1
- Fix changelog order
- Improve defined function macros
- Improve scriptlets
- Add dependency for v2ray_path
- Change summary and url
- Add real license

* Tue Sep 22 2020 sixg0000d <sixg0000d@gmail.com> - 1.0.2 - 1
- Fix can not remove when v2ray not exists

* Tue Sep 22 2020 sixg0000d <sixg0000d@gmail.com> - 1.0.1 - 1
- Remove build arch

* Tue Sep 22 2020 sixg0000d <sixg0000d@gmail.com> - 1.0.0 - 1
- Inital v2ray-cap
