cmake_minimum_required(VERSION 3.16)
project(VTide Fortran)

include(FindLAPACK)
if (NOT ${LAPACK_FOUND})
  message (FATAL_ERROR "LAPACK is not found.")
endif()

if ("${CMAKE_Fortran_COMPILER_ID}" MATCHES "Intel")
  set (CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -extend-source")
elseif ("${CMAKE_Fortran_COMPILER_ID}" MATCHES "GNU")
  set (CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -ffixed-line-length-0")
else ()
  message (FATAL_ERROR "Not supported compiler: ${CMAKE_Fortran_COMPILER_ID")
endif()

add_library(versatile_tide analyze.for astro_time.for constituents.for file_io.for predict.for svd.for write_output.for)

add_executable(vt_analyze analyze_driver.for)
target_link_libraries(vt_analyze versatile_tide ${LAPACK_LIBRARIES})

add_executable(vt_predict predict_driver.for)
target_link_libraries(vt_predict versatile_tide ${LAPACK_LIBRARIES})