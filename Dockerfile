FROM ubuntu

# Install useful C/C++ dev tools
RUN apt-get update -qq
RUN apt-get -qq install -y \
  cdecl \
  clang \
  clang-tools \
  git \
  lldb \
  make \
  man \
  manpages \
  manpages-dev \
  manpages-posix \
  manpages-posix-dev \
  perl \
  valgrind \
  vim \
  && rm -rf /var/lib/apt/lists/*

# Set up man pages
RUN cd /tmp && git clone http://git.kernel.org/pub/scm/docs/man-pages/man-pages
RUN cd /tmp/man-pages && make install
RUN mandb
RUN rm -r /tmp/man-pages
