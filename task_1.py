def func(name, **infos):
    print(name)
    for info, value in infos.items():
        print(f'{info} - {value}')
func(name='USA', population='330 million', is_democratic=True)
func(name='Kyrgyzstan', area='200 km2', have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])