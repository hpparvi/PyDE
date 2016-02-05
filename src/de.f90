module de_f
use omp_lib
implicit none

contains 
  subroutine evolve_population(pop, f, c, ndim, npop, pout)
    implicit none
    integer, intent(in) :: ndim, npop
    real(8), intent(in) :: f, c
    real(8), intent(in),  dimension(npop,ndim) :: pop
    real(8), intent(out), dimension(npop,ndim) :: pout
    integer :: i

    ! $omp parallel do shared(pop,f,c,ndim,npop,pout) private(i)
    do i=0,npop-1
       call evolve_pv(i, pop, f, c, ndim, npop, pout(i+1,:))
    end do
    ! $omp end parallel do
  end subroutine evolve_population


  subroutine evolve_pv(i, pop, f, c, ndim, npop, vout)
    implicit none
    integer, intent(in) :: i, ndim, npop
    real(8), intent(in) :: f, c
    real(8), intent(in),  dimension(npop,ndim) :: pop
    real(8), intent(out), dimension(ndim) :: vout
    integer :: j, ids(3)
    real(8), dimension(ndim) :: co, v
    real(8) :: x

    ids = i+1
    do while (ids(1) == i+1)
       call random_number(x)
       ids(1) = floor(x*npop) + 1
    end do
    do while ((ids(2) == i+1) .or. (ids(2) == ids(1)))
       call random_number(x)
       ids(2) = floor(x*npop) + 1
    end do
    do while ((ids(3) == i+1) .or. (ids(3) == ids(2)) .or. (ids(3) == ids(1)))
       call random_number(x)
       ids(3) = floor(x*npop) + 1
    end do

    v = pop(ids(1),:) + f * (pop(ids(2),:) - pop(ids(3),:))

    !! --- CROSS OVER ---
    call random_number(co)
    where (co <= c)
       vout = v
    elsewhere
       vout = pop(i+1,:)
    end where

    !! --- FORCED CROSSING -- -
    call random_number(x)
    j = floor(x*ndim) + 1
    vout(j) = v(j)

  end subroutine evolve_pv
end module de_f
