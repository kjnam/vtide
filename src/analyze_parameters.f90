module analyze_parameters
  use constituent

  implicit none
  integer, parameter :: kin = 4      !< unit number for the main input file
  integer, parameter :: max_main_cnstnt = 80
  integer, parameter :: max_infer = 80
  integer, parameter :: mcc = 70       !< max allowed consituent estimates
  integer, parameter :: nmaxp1 = mc*2  !< dimension 'at least as great as the number of variables'
end module
