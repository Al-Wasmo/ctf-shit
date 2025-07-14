ssize_t __fastcall write(int fd, const void *buf, size_t size)
{
  size_t v4; // rax
  size_t v5; // r13
  Fd *v6; // rdi
  __int64 v7; // rax
  __int64 v8; // rbx
  __int64 v9; // rax
  char *v10; // r8
  __int64 v11; // rdx
  __int64 v13; // rax
  iovec iov; // [rsp+0h] [rbp-30h] BYREF

  v4 = 2147479552LL;
  if ( size <= 0x7FFFF000 )
    v4 = size;
  v5 = v4;
  if ( fd < 0 )
    goto LABEL_11;
  if ( fd >= g_fds.n )
  {
    if ( ((unsigned __int8)_hostos & 0x79) != 0 )
      goto LABEL_21;
LABEL_11:
    ebadf();
    v8 = v9;
    goto LABEL_12;
  }
  v6 = &g_fds.p[(__int64)fd];
  if ( v6->kind == 6 )
    goto LABEL_11;
  if ( ((unsigned __int8)_hostos & 0x79) != 0 )
  {
LABEL_21:
    sys_write();
    v8 = v13;
    goto LABEL_12;
  }
  if ( ((unsigned __int8)_hostos & 2) != 0 )
  {
    iov.iov_base = (void *)buf;
    iov.iov_len = v4;
    v8 = sys_writev_metal(v6, &iov, 1);
  }
  else if ( ((unsigned __int8)_hostos & 4) != 0 )
  {
    iov.iov_base = (void *)buf;
    iov.iov_len = v4;
    v8 = sys_writev_nt(fd, &iov, 1);
  }
  else
  {
    enosys();
    v8 = v7;
  }
LABEL_12:
  if ( strace_enabled(0) > 0 )
  {
    v10 = "\b \b" + 3;
    if ( v8 >= 41 )
      v10 = "...";
    v11 = 40LL;
    if ( v8 <= 40 )
      v11 = v8;
    if ( v11 < 0 )
      v11 = 0LL;
    _stracef(aRsys6p6h18tWri, (unsigned int)fd, v11, buf, v10, v5, v8);
  }
  return v8;
}