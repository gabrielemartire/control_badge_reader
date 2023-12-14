
# CONTROL BADGE RE▲DER

## ***Project description***
> _The chosen case study is about the management of access via employee identification badges in a private research institute, divided into sectors, which are in turn divided into smaller areas._
+ Gabriele Martire
+ Corso di studi in Ingegneria Industriale L-9
+ Etivities per ‘Basi di Dati’
+ [Report sviluppo progetto](https://github.com/gabrielemartire/control_badge_reader/blob/master/c_b_r_report.pdf)

## ***Installation***
### PyMySQL and SQLAlchemy
```
>pip install PyMySQL
```
```
>pip install SQLAlchemy
```
### cryptography 
> [!WARNING]
> may also require cryptography to be installed.
```
>pip install cryptography
```
## ***Run***
1) ### activate _env_
```
>env\Scripts\activate
```
2) ### execute code
```
(env) >python main.py
```
Once `main.py` is launched, the 'models menu' selection screen will be shown:
```python
----------Models Menu----------
1 - ROLES
2 - USERS
3 - BADGES
4 - BADGES_READER
5 - ACCESS
6 - SECTOR
7 - WARNING
8 - RELATIONS
9 - SEEDs
0 - EXIT
select model:
```
Subsequently we will choose the action from those available (`5 - ACCESS` in this example), after that the 'available actions' selection screen will be shown:
```python
available actions:
1 - ENTER A SPECIFIC AREA WITH A SPECIFIC BADGE (create new access)
2 - SHOW ACCESS LOG (retrieve an access)
3 - EXIT A SPECIFIC AREA WITH A SPECIFIC BADGE (update an access)
0 - back
select action:
```
At this point by following the instructions on the screen you can complete the requested operation.
> _for example enter (action=1) with a 'Security Chief' badge (id=5) in the 'Control room' area (id=10)_
```python
select action: 1
insert badge id: 5
insert badge reader id: 10
```
Obtaining authorization to enter:
```python
authorized
```
3) ### seed :shipit:
> [!IMPORTANT]
> It is also possible to use seed to quickly generate useful data with different combinations of values for test.
```python
# SEED USERS
for u in USERS:
   create_user(session = session, user_info = u)
```
By selecting option `9 - SEEDs` in 'models menu':
```
data creation from seed finished
```
Once the data has been created, a confirmation message will be shown.
