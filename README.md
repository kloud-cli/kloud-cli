# KLOUD-CLI

A lightweight CLI that supports public clouds in a simple and agnostic way.  We proudly leverage the 
[apache-libcloud](https://github.com/apache/libcloud) project under the covers to help mask the competing 
complexities of vendor specifc API's.

## Vocabulary

- **Provider**: Supported cloud providers include AWS, Azure, EquinixMetal, & Akamai-Linode

- **Airport**: Three character international airport codes are consistently mapped to Provider
           specific Region codes

- **VM**: A compute Virtual Machine

## Installation (eventually)

`pip install kloud-cli`

## Usage Examples

`kloud --help`

`kloud provider list`

`kloud airport list`

`kloud vm --help`
