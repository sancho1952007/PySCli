# PySCli

## **About:**
A Simple Python Module to get User - Terminal Commands

<br><br>

## **How To Install?**
***Windows***:
```cmd
python -m pip install git+https://github.com/sancho1952007/PySCli.git
```

<br>

***Linux:***
```bash
python3 -m pip install git+https://github.com/sancho1952007/PySCli.git
```

<br><br>

## **How To Preview The Module After Installation?**
***Windows:***
```cmd
python -m pyscli
```

<br>

***Linux:***
```bash
python3 -m pyscli
```

## **How to Use PySCli?**
```python
import pyscli
cmd=cli('--hello', sensitive=False)
print(cmd)
```

This Will Return True If User Enters *Windows: `your-file.py --hello`* or *Linux: `python3 your-file.py --hello`*. Else, It Will Return False.  

It Detects Extra Arguments eg: `--user, --hi, --hello, and Custom Arguments`!  

You Can Add Unlimited Arguments! But, Remember: USE `sensitive` keyword to keep argument Case Sensitive ot NOT!  
eg: `sensitive=True` or `sensitive=False`
