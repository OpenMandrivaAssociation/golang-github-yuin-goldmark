# Run tests in check section
# FIXME: fails on aarch64
%bcond_with check

# https://github.com/yuin/goldmark
%global goipath		github.com/yuin/goldmark
%global forgeurl	https://github.com/yuin/goldmark
Version:		1.7.8

%gometa

Summary:	A markdown parser written in Go
Name:		golang-github-yuin-goldmark

Release:	1
Source0:	https://github.com/yuin/goldmark/archive/v%{version}/goldmark-%{version}.tar.gz
URL:		https://github.com/yuin/goldmark
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
A markdown parser written in Go.

Main features:
 *  Easy to extend
        Markdown is poor in document expressions
        compared to other light markup languages
        such as reStructuredText.  We have extensions
        to the Markdown syntax, e.g. PHP Markdown
        Extra, GitHub Flavored Markdown.
 *   Standards-compliant
        Markdown has many dialects.  GitHub-Flavored
        Markdown is widely used and is based upon
        CommonMark, effectively mooting the question
        of whether or not CommonMark is an ideal specification.
        CommonMark is complicated and hard to implement.
 *   Well-structured
        AST-based; preserves source position of nodes.
 *   Written in pure Go

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n goldmark-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

