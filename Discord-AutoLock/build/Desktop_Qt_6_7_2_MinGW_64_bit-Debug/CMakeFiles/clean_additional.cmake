# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\Discord-AutoLock_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\Discord-AutoLock_autogen.dir\\ParseCache.txt"
  "Discord-AutoLock_autogen"
  )
endif()
