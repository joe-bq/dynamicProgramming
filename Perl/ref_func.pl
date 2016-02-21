# file - ref_func.pl
# description: this file will demonstrate the use of the scalar reference and discover the real type of the object that 
#   is pointed by the scalar references

use warnings;
use Carp;
use strict;
# ref function 
#   http://perldoc.perl.org/functions/ref.html
# there are 11 types of object that we can create a reference to 
#
#   SCALAR
#   ARRAY
#   HASH
#   CODE
#   REF
#   GLOB
#   LVALUE
#   FORMAT
#   IO
#   VSTRING
#   Regexp
# 

sub sub_routine() {
 
}

sub main() { 
  #my ($scalar), @array, %hash);
  my $scalar_obj = "";
  my @array = ();
  my %hash = ();
  
  my $scalar_ref = \$scalar_obj;
  my $array_ref = \@array;
  my $hash_ref = \%hash;
  
  my $routine_ref = \&sub_routine;
  
  my $regexp_ref = qr(hello); #
  
  my $scalar_ref_ref = \$scalar_ref;
  
  #open (FILE_H, "ref_func.pl");
  open(my $file, "ref_func.pl");
  
  open(FILE_H, "ref_func.pl");
  # perlref 
  #   http://perldoc.perl.org/perlref.html
  # see also the way to disambiguate hash reference and function block 
  # with the help of '+' and ';'
  # 
  my $file_h = \*FILE_H;  

  # you can ignore the code below   
  *file_h = \$scalar_ref;
  *foo = \&sub_routine;
  *a = *b; 
  
  #Format
  #  http://perldoc.perl.org/functions/format.html
  my $str;
  my $num ;
  my $cost = 100;
  my $quality = 19;
  format Something = 
     Test: @<<<< @|||||| @>>>>
            $str, $%, '$' . int ($num)
.
  
  $str = "widget";
  $num = $cost/$quality;
  $~ = 'Something';
  
  # perlref
  #   http://perldoc.perl.org/perlref.html
  # in Making References. point 7, the special syntax to create references, because IO handles and format are not easy to create references
  #   
  my $format_ref = *Something{FORMAT};
  
  my $io_ref = *STDIN{IO};
  
  printf("\$scalar_ref = %s\n", ref($scalar_ref));
  printf("\$array_ref = %s\n", ref($array_ref));
  printf("\$hash_ref = %s\n", ref($hash_ref));
  printf("\$routine_ref = %s\n", ref($routine_ref));
  printf("\$regexp_ref = %s\n", ref($regexp_ref));  # this will print Regexp
  printf("\$scalar_ref_ref = %s\n", ref($scalar_ref_ref)); # this will print REF, because $scalar_ref_ref is the reference to the reference
  printf("\$file = %s\n", ref($file)); # this will  print GLOB, because this is a file handler
  printf("\$file_h = %s\n", ref($file_h)); # this wil print GLOB 
  printf("\$format_ref = %s\n", ref($format_ref)); # this will print FORMAT
  printf("\$io_ref = %s\n", ref($io_ref)); # this will print IO
  
  
  # ===================================
  #  LVALUE and VSTRING references are special references which is not illustrate here, 
  # see more details on how this variables are created. 
  #   http://perldoc.perl.org/functions/ref.html
  # QUOTE:  "The return value LVALUE indicates a reference to an lvalue that is not a variable. You get this from taking the reference of function calls like pos() or substr(). VSTRING is returned if the reference points to a version string."
  # 
  # ===================================
}

main();