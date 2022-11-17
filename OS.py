import platform
import os
try:
  import distro
except:
  None
def os_main():
  OS = platform.platform()[:5].lower()
  if OS == "linux":
    try:
      distribution = distro.id()
    except:
      distribution = "N/A"
  elif not platform == "linux":
    distribution = None
  print(OS)
  print(distribution)
  os.system('uname -m')
