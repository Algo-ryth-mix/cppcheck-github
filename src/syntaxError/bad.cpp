#include <type_traits>

template<typename derived_type, typename base_type>
using inherits_from = typename std::enable_if<
    std::is_base_of<base_type, derived_type>::value, int>::type;


template <class T>
struct Foo {};

struct Bar : Foo<Bar> {};

template <typename T, inherits_from<T,Foo<T>> = 0>
void baz(T t){}

int main()
{
    baz(Bar{});
}