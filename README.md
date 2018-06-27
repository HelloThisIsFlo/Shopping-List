# Shopping List - Do More, Pay Less

`shopping_list` is a simple tool to calculate the cost breakdown and total of a shopping list containing items in multiple categories.

It allows to create **different variation of prices**, to compare the influence in the total cost.  
See the corresponding section [Pro Tip - Price combinations](#pro-tip---price-combinations)

## `shopping_list` in action
The project was originally created to estimate the total cost of devices in a Home-Automation project and **see the influence of different purchase decisions**.

#### Given:
* A list of prices
* A shopping list of items per category (per room in the example)

#### It generates an output breaking down the costs.


```shell
> shoppinglist shopping_list.yaml prices.yaml 

Total cost breakdown

---
Living Room: 77.5 €
Kitchen: 45 €
Extra: 15 €
---

Total: 137.5 €

```

#### With `shopping_list.yaml`
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

#### And `prices.yaml`
```yaml
InWallSwitch: 26
PaddleSwitch: 15

MotionSensor: 10.5

BulbBasic: 15
BulbAmbiance: 30

Shipping: 15
```


#### Demo versions of these files can be find under `demo/`  
```shell
shoppinglist demo/shopping_list.yaml demo/prices.yaml
```

## Usage
### Installation
```bash
pip install shoppinglist
```

### Usage
```
Usage: shoppinglist [OPTIONS] SHOPPING_LIST_FILE PRICES_FILE
                       [PRICE_OVERRIDES_FILES]...

Options:
  --with-count  Display the count for each item
  --help        Show this message and exit.
```
#### Arguments
##### `SHOPPING_LIST_FILE`
* The shopping list
* `shopping_list.yaml` in the previous examples

##### `PRICES_FILE`
* The base prices
* `prices.yaml` in the previous examples

##### `[PRICE_OVERRIDES_FILES]`
* Zero or multiple _price overrides files_
* A _price override_ has the same format as the `PRICES_FILE` file
* `PRICE_OVERRIDES_FILES` define prices overridings the base prices present in `PRICES_FILE`
* Kinda like _mixins_ for the price list
* In case of _multiple overrides_, only the _last one_ is taken into account

#### Format for the files
##### `prices.yaml` and `price_overrides_*.yaml`
* 1 item per line, with its price
* See example

##### `shopping_list.yaml`
* 1 block per category
* Each block contains a list on items
* Item prices must have been defined in `prices.yaml`
* Duplicates allowed, they will be counted twice
* See example

## Pro Tip - Price combinations
Create different combination of **prices** to see quickly see the influence of your purchase decisions.

#### To do so, you have 2 options:
* Define **multiple base prices**
* Define **a base price** and **override individual items**

### Using multiple base prices
##### For instance `amazon.yaml`
```yaml
InWallSwitch: 56 <- More expensive InWallSwitch
PaddleSwitch: 7  <- Cheaper PaddleSwitch

MotionSensor: 10.5

BulbBasic: 15
BulbAmbiance: 30

Shipping: 0      <- Free shipping
```

##### Or `upgrade_basic_to_ambiance.yaml`
```yaml
InWallSwitch: 26
PaddleSwitch: 15

MotionSensor: 10.5

BulbBasic: 30     <- Bump the price of 'basic' bulb to match
BulbAmbiance: 30     the one of the 'ambiance' variation
                     and see how it affects the Total!
Shipping: 15
```

##### Results
```shell
> shoppinglist demo/shopping_list.yaml demo/prices.yaml
...
Total: 137.5 €

> shoppinglist demo/shopping_list.yaml demo/amazon.yaml 
...
Total: 174.5 €

> shoppinglist demo/shopping_list.yaml demo/upgrade_basic_to_ambiance.yaml
...
Total: 152.5 €
```


### Using prices overrides
##### With base `prices.yaml`
```yaml
InWallSwitch: 26
PaddleSwitch: 15

MotionSensor: 10.5

BulbBasic: 15
BulbAmbiance: 30

Shipping: 15
```

##### First override `free_shipping.yaml`
```yaml
Shipping: 0 <- Free shipping
```

##### Second override `tradfri_bulb_instead_of_hue.yaml`
```yaml
BulbBasic: 10    <- Cheaper Bulbs
BulbAmbiance: 20 <- Cheaper Bulbs
```

##### Results
```shell
> shoppinglist demo/shopping_list.yaml demo/prices.yaml
...
Total: 137.5 €

> shoppinglist demo/shopping_list.yaml demo/prices.yaml demo/free_shipping.yaml
...
Total: 122.5 €

> shoppinglist demo/shopping_list.yaml demo/prices.yaml demo/free_shipping.yaml demo/tradfri_bulb_instead_of_hue.yaml
...
Total: 107.5 €
```

## Development
### Prerequisites: Pipenv
This project needs `pipenv` in order to work.

If you haven't set it up already... please do yourself a favor and read about it. That thing made my life just slightly better... but to the point where I actually notice an increase in my mood while working with python projects.   
Kudos to them :)

More info on: [Pipenv: Python Development Workflow for Humans](https://github.com/pypa/pipenv)

**Interested in having that setup automatically for you?**  
Then check out my ansible role that does just that ;)  
**==>** [FlorianKempenich.python-virtualenv](https://github.com/FlorianKempenich/ansible-role-python-virtualenv)

### Installation
```bash
git clone git@github.com:FlorianKempenich/Shopping-List.git
cd Shopping-List
pipenv install --dev
pipenv shell
```

### Tests
```bash
pytest
# Or
./start_tdd.sh
```





## Author Information
Follow me on Twitter: [@ThisIsFlorianK](https://twitter.com/ThisIsFlorianK)  
Find out more about my work: [Florian Kempenich - Personal Website](https://floriankempenich.com)
