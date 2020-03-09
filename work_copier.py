# useful tool for copying partner work
import os

partner_pd = 1
partner_first = 'Ivan'
partner_last = 'Galakhov'
partner_num = '00'
work_name = '11_mongo-flask'

if __name__ == '__main__':
    submodule_name = str(partner_pd) + '/' + (partner_first[0] + partner_last + partner_num).lower()
    print('Getting [%s] from %s %s in period %d' %
          (work_name, partner_first, partner_last, partner_pd))
    os.system(
        'git clone https://github.com/stuy-softdev/workshop19-20 temp/workshop/'
    )
    os.chdir('temp/workshop')
    os.system('git submodule update --remote --init %s' % submodule_name)
    os.chdir('../..')
    os.system('rm -rf %s' % work_name)
    os.system('mkdir %s' % work_name)
    os.system('mv temp/workshop/%s/%s .' % (submodule_name, work_name))
    os.system('rm -rf temp')
    print('Done!')
