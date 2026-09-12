Name:		python-tiktoken
Version:	0.14.0
Release:	1
Summary:	Fast BPE tokeniser for OpenAI models
License:	MIT
Group:		Development/Python
URL:		https://github.com/openai/tiktoken
Source0:	https://files.pythonhosted.org/packages/source/t/tiktoken/tiktoken-%{version}.tar.gz
Source1:	cargo-vendor-for-tiktoken-%{version}.tar.xz
Source2:	cargo-config.toml
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-rust)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	cargo
BuildRequires:	rust-packaging
BuildRequires:	clang
Requires:	python%{pyver}dist(regex)
Requires:	python%{pyver}dist(requests)

%description
tiktoken is OpenAI's fast BPE tokeniser. Required by LiteLLM / Aider.

%prep
%autosetup -n tiktoken-%{version}
tar -xf %{SOURCE1}
install -D -m 0644 %{SOURCE2} .cargo/config.toml
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true

%build

%install
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
export CC=clang
export CXX=clang++
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tiktoken
%{python_sitearch}/tiktoken_ext
%{python_sitearch}/tiktoken-*.*-info
