# Shopping List - Cost breakdown calculator


`shopping_list` is a simple tool to calculate the cost breakdown and total of a shopping list containing items in multiple categories.

It allows to create **different variation of prices**, to compare the influence in the total cost.

## `shopping_list` in action
The project was originally created to estimate the total cost of devices in a Home-Automation project and **see the influence of different purchase decisions**.

#### Given:
* A list of prices
* A shopping list of items per category (per room in the example)

#### It generates an output breaking down the costs.


```shell
> ./shopping_list prices.yaml shopping_list.yaml

Total cost breakdown

---
Living Room: 77.5 €
Kitchen: 45 €
Extra: 15 €
---

Total: 137.5 €

```

#### With `prices.yaml`
```yaml
InWallSwitch: 26
PaddleSwitch: 15

MotionSensor: 10.5

BulbBasic: 15
BulbAmbiance: 30

Shipping: 15
```

#### And `shopping_list.yaml`
```yaml
Living-room:
  - InWallSwitch
  - InWallSwitch
  - PaddleSwitch
  - MotionSensor

Kitchen:
  - BulbBasic
  - BulbAmbiance

Extra:
  - Shipping
```

#### Demo versions of these files can be find under `demo/`  
```shell
./shopping_list demo/prices.yaml demo/shopping_list.yaml
```

## Usage
### Prerequisites: Pipenv
This project needs `pipenv` in order to work.

If you haven't set it up already... please do yourself a favor and read about it. That thing made my life just slightly better... but to the point where I actually notice an increase in my mood while working with python projects.   
Kudos to them :)

More info on: [Pipenv: Python Development Workflow for Humans](https://github.com/pypa/pipenv)

**Interested in having that setup automatically for you?**  
Then check out my ansible role that does just that ;)  
**==>** [FlorianKempenich.python-virtualenv](https://github.com/FlorianKempenich/ansible-role-python-virtualenv)

### Installation
```
git clone git@github.com:FlorianKempenich/Shopping-List.git
cd Shopping-List
pipenv install
# Or, for development purposes
pipenv install --dev && pipenv shell
```

### Usage
```
./shopping_list PRICES_FILE SHOPPING_LIST_FILE

# Or

./shopping_list --with-count PRICES_FILE SHOPPING_LIST_FILE
```

#### Format for the files
##### `prices.yaml`
* 1 item per line, with its price
* See example

##### `shopping_list.yaml`
* 1 block per category
* Each block contains a list on items
* Item prices must have been defined in `prices.yaml`
* Duplicates allowed, they will be counted twice
* See example

## Pro Tip
Create different combination of **prices** to see quickly see the influence of your purchase decisions.
##### For instance `amazon.yaml`
```yaml
InWallSwitch: 56 <- More expensive InWallSwitch
PaddleSwitch: 7  <- Cheaper PaddleSwitch

MotionSensor: 10.5

BulbBasic: 15
BulbAmbiance: 30

Shipping: 0      <- Free shipping
```

#### Or: `upgrade_basic_to_ambiance.yaml`
```yaml
InWallSwitch: 26
PaddleSwitch: 15

MotionSensor: 10.5

BulbBasic: 30     <- Bump the price of 'basic' bulb to match
BulbAmbiance: 30     the one of the 'ambiance' variation
                     and see how it affects the Total!
Shipping: 15
```

## Author Information
Follow me on Twitter: [@ThisIsFlorianK](https://twitter.com/ThisIsFlorianK)  
Find out more about my work: [Florian Kempenich - Personal Website](https://floriankempenich.com)
