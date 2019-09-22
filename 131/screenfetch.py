import re

output = """
                                       mohh@SERENiTY
 MMMMMMMMMMMMMMMMMMMMMMMMMmds+.        OS: Mint 19 tara
 MMm----::-://////////////oymNMd+'     Kernel: x86_64 Linux 4.15.0-34-generic
 MMd      /++                -sNMd:    Uptime: 1d 4m
 MMNso/'  dMM    '.::-. .-::.' .hMN:   Packages: 2351
 ddddMMh  dMM   :hNMNMNhNMNMNh: 'NMm   Shell: zsh 5.4.2
     NMm  dMM  .NMN/-+MMM+-/NMN' dMM   Resolution: 1366x768
     NMm  dMM  -MMm  'MMM   dMM. dMM   DE: Cinnamon 3.8.9
     NMm  dMM  -MMm  'MMM   dMM. dMM   WM: Muffin
     NMm  dMM  .mmd  'mmm   yMM. dMM   WM Theme: Linux Mint (Mint-Y)
     NMm  dMM'  ..'   ...   ydm. dMM   GTK Theme: Mint-Y [GTK2/3]
     hMM- +MMd/-------...-:sdds  dMM   Icon Theme: Mint-Y
     -NMm- :hNMNNNmdddddddddy/'  dMM   Font: Noto Sans 9
      -dMNs-''-::::-------.''    dMM   CPU: AMD A10-7400P Radeon R6, 10 Compute Cores 4C+6G @ 4x 2.5GHz [101.0°C]
       '/dMNmy+/:-------------:/yMMM   GPU: AMD KAVERI (DRM 2.50.0 / 4.15.0-34-generic, LLVM 6.0.0)
          ./ydNMMMMMMMMMMMMMMMMMMMMM   RAM: 1886MiB / 6915MiB
             \.MMMMMMMMMMMMMMMMMMM
"""

debian = """
         _,met$$$$$gg.           mohh@SERENiTY
      ,g$$$$$$$$$$$$$$$P.        OS: Mint 19 tara
    ,g$$P""       ""'Y$$.".      Kernel: x86_64 Linux 4.15.0-34-generic
   ,$$P'              '$$$.      Uptime: 1d 2h 50m
  ',$$P       ,ggs.     '$$b:    Packages: 2352
  'd$$'     ,$P"'   .    $$$     Shell: zsh 5.4.2
   $$P      d$'     ,    $$P     Resolution: 1366x768
   $$:      $$.   -    ,d$$'     DE: Cinnamon 3.8.9
   $$\;      Y$b._   _,d$P'      WM: Muffin
   Y$$.    '.'"Y$$$$P"'          WM Theme: Linux Mint (Mint-Y)
   '$$b      "-.__               GTK Theme: Mint-Y [GTK2/3]
    'Y$$                         Icon Theme: Mint-Y
     'Y$$.                       Font: Noto Sans 9
       '$$b.                     CPU: AMD A10-7400P Radeon R6, 10 Compute Cores 4C+6G @ 4x 2.5GHz [101.0°C]
         'Y$$b.                  GPU: AMD KAVERI (DRM 2.50.0 / 4.15.0-34-generic, LLVM 6.0.0)
            '"Y$b._              RAM: 2429MiB / 6915MiB
                '"'""
"""
mac = """
                -/+:.          ejo@BlackOil
               :++++.          OS: 64bit Mac OS X 10.13.6 17G65
              /+++/.           Kernel: x86_64 Darwin 17.7.0
      .:-::- .+/:-''.::-       Uptime: 1d 49m
   .:/++++++/::::/++++++/:'    Packages: 236
 .:///////////////////////:'   Shell: bash 4.4.23
 ////////////////////////'     Resolution: 2560x1600
-+++++++++++++++++++++++'      DE: Aqua
/++++++++++++++++++++++/       WM: Quartz Compositor
/sssssssssssssssssssssss.      WM Theme: Blue
:ssssssssssssssssssssssss-     Font: SourceCodePro-Medium
 osssssssssssssssssssssssso/'  CPU: Intel Core i7-4980HQ @ 2.80GHz
 'syyyyyyyyyyyyyyyyyyyyyyyy+'  GPU: Intel Iris Pro / NVIDIA GeForce GT 750M
  'ossssssssssssssssssssss/    RAM: 9960MiB / 16384MiB
    :ooooooooooooooooooo+.
     ':+oo+/:-..-:/+o+/-
"""


def _get_kw_value(output, keyword):

  pattern = r'{}:(.*)\n'.format(keyword)
  m = re.search(pattern, output)

  return m.group(1).strip() if m else ''


def sysinfo_scrape(output):
  """Scrapes the output from screenfetch and returns a dictionary"""

  key_list = ['Name', 'OS', 'Kernel', 'Uptime', 'Packages', 'Shell', 'Resolution', 'DE', 'WM', 'WM Theme', 'GTK Theme', 'Icon Theme', 'Font', 'CPU', 'GPU', 'RAM']

  scraped = dict.fromkeys(key_list)

  name_pattern = r'\s+([^\s]*)\n'
  m = re.search(name_pattern, output)
  name = m.group(1).strip() if m else ''
  scraped['Name'] = name

  for kw in key_list[1:]:
    scraped[kw] = _get_kw_value(output, kw)

  return scraped


# def main():

#   print('here ...')

#   s = sysinfo_scrape(output)
#   assert isinstance(s, dict)
#   assert s["Name"] == "mohh@SERENiTY"
#   assert len(s) == 16

#   expected = [
#       'Name', 'OS', 'Kernel', 'Uptime', 'Packages', 'Shell',
#       'Resolution', 'DE', 'WM', 'WM Theme', 'GTK Theme', 'Icon Theme',
#       'Font', 'CPU', 'GPU', 'RAM'
#   ]
#   assert list(s.keys()) == expected

#   expected = [
#       'mohh@SERENiTY', 'Mint 19 tara', 'x86_64 Linux 4.15.0-34-generic',
#       '1d 4m', '2351', 'zsh 5.4.2', '1366x768', 'Cinnamon 3.8.9', 'Muffin',
#       'Linux Mint (Mint-Y)', 'Mint-Y [GTK2/3]', 'Mint-Y', 'Noto Sans 9',
#       'AMD A10-7400P Radeon R6, 10 Compute Cores 4C+6G @ 4x 2.5GHz [101.0°C]',
#       'AMD KAVERI (DRM 2.50.0 / 4.15.0-34-generic, LLVM 6.0.0)',
#       '1886MiB / 6915MiB'
#   ]
#   assert list(s.values()) == expected

#   sysinfo = sysinfo_scrape(debian)
#   assert sysinfo["Resolution"] == "1366x768"

#   sysinfo = sysinfo_scrape(mac)
#   assert sysinfo["Name"] == "ejo@BlackOil"
#   # print(sysinfo_scrape(debian))
#   # print(sysinfo_scrape(mac))


# if __name__ == '__main__':
#   main()
