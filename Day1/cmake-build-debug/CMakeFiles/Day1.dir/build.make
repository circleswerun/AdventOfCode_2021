# CMAKE generated file: DO NOT EDIT!
# Generated by "NMake Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

!IF "$(OS)" == "Windows_NT"
NULL=
!ELSE
NULL=nul
!ENDIF
SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2021.2.3\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2021.2.3\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\AdventOfCode_2021\Day1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\AdventOfCode_2021\Day1\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles\Day1.dir\depend.make
# Include the progress variables for this target.
include CMakeFiles\Day1.dir\progress.make

# Include the compile flags for this target's objects.
include CMakeFiles\Day1.dir\flags.make

CMakeFiles\Day1.dir\main.cpp.obj: CMakeFiles\Day1.dir\flags.make
CMakeFiles\Day1.dir\main.cpp.obj: ..\main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\AdventOfCode_2021\Day1\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Day1.dir/main.cpp.obj"
	C:\PROGRA~2\MICROS~3\2019\COMMUN~1\VC\Tools\MSVC\1429~1.300\bin\Hostx86\x86\cl.exe @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) /FoCMakeFiles\Day1.dir\main.cpp.obj /FdCMakeFiles\Day1.dir\ /FS -c D:\AdventOfCode_2021\Day1\main.cpp
<<

CMakeFiles\Day1.dir\main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Day1.dir/main.cpp.i"
	C:\PROGRA~2\MICROS~3\2019\COMMUN~1\VC\Tools\MSVC\1429~1.300\bin\Hostx86\x86\cl.exe > CMakeFiles\Day1.dir\main.cpp.i @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\AdventOfCode_2021\Day1\main.cpp
<<

CMakeFiles\Day1.dir\main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Day1.dir/main.cpp.s"
	C:\PROGRA~2\MICROS~3\2019\COMMUN~1\VC\Tools\MSVC\1429~1.300\bin\Hostx86\x86\cl.exe @<<
 /nologo /TP $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) /FoNUL /FAs /FaCMakeFiles\Day1.dir\main.cpp.s /c D:\AdventOfCode_2021\Day1\main.cpp
<<

# Object files for target Day1
Day1_OBJECTS = \
"CMakeFiles\Day1.dir\main.cpp.obj"

# External object files for target Day1
Day1_EXTERNAL_OBJECTS =

Day1.exe: CMakeFiles\Day1.dir\main.cpp.obj
Day1.exe: CMakeFiles\Day1.dir\build.make
Day1.exe: CMakeFiles\Day1.dir\objects1.rsp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\AdventOfCode_2021\Day1\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Day1.exe"
	"C:\Program Files\JetBrains\CLion 2021.2.3\bin\cmake\win\bin\cmake.exe" -E vs_link_exe --intdir=CMakeFiles\Day1.dir --rc=C:\PROGRA~2\WI3CF2~1\10\bin\100190~1.0\x86\rc.exe --mt=C:\PROGRA~2\WI3CF2~1\10\bin\100190~1.0\x86\mt.exe --manifests -- C:\PROGRA~2\MICROS~3\2019\COMMUN~1\VC\Tools\MSVC\1429~1.300\bin\Hostx86\x86\link.exe /nologo @CMakeFiles\Day1.dir\objects1.rsp @<<
 /out:Day1.exe /implib:Day1.lib /pdb:D:\AdventOfCode_2021\Day1\cmake-build-debug\Day1.pdb /version:0.0 /machine:X86 /debug /INCREMENTAL /subsystem:console  kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib 
<<

# Rule to build all files generated by this target.
CMakeFiles\Day1.dir\build: Day1.exe
.PHONY : CMakeFiles\Day1.dir\build

CMakeFiles\Day1.dir\clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Day1.dir\cmake_clean.cmake
.PHONY : CMakeFiles\Day1.dir\clean

CMakeFiles\Day1.dir\depend:
	$(CMAKE_COMMAND) -E cmake_depends "NMake Makefiles" D:\AdventOfCode_2021\Day1 D:\AdventOfCode_2021\Day1 D:\AdventOfCode_2021\Day1\cmake-build-debug D:\AdventOfCode_2021\Day1\cmake-build-debug D:\AdventOfCode_2021\Day1\cmake-build-debug\CMakeFiles\Day1.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles\Day1.dir\depend

