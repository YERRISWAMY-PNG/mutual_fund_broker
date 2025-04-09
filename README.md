# Mutual Fund Broker Web Application

A Django backend application for a mutual fund brokerage platform with RapidAPI integration, user authentication, and portfolio tracking.

## Features

- User registration and authentication (email + password)
- Fund family selection and open-ended mutual fund data fetching
- Portfolio management with current value tracking
- Integration with [Latest Mutual Fund NAV API](https://rapidapi.com/suneetk92/api/latest-mutual-fund-nav) via RapidAPI
- RESTful API endpoints for all operations

## Technologies Used

- **Backend**: Django 4.2, Django REST Framework
- **Database**: SQLite (default, can be configured for PostgreSQL/MySQL)
- **API Integration**: RapidAPI Mutual Fund NAV API
- **Authentication**: Token-based authentication

## Setup Instructions

### Prerequisites

- Python 3.8+
- RapidAPI account (free tier available)
- Postman (for API testing)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YERRISWAMY-PNG/mutual_fund_broker.git
   cd mutual_fund_broker
   
### Postman Collection:
{
  "info": {
    "_postman_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
    "name": "Mutual Fund Broker API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Auth",
      "item": [
        {
          "name": "Register",
          "request": {
            "method": "POST",
            "header": [],
            "body": {
              "mode": "raw",
              "raw": "{\n    \"email\": \"test@example.com\",\n    \"username\": \"testuser\",\n    \"password\": \"testpass123\"\n}",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "{{base_url}}/api/auth/register/",
              "host": [
                "{{base_url}}"
              ],
              "path": [
                "api",
                "auth",
                "register",
                ""
              ]
            }
          },
          "response": []
        },
        {
          "name": "Login",
          "request": {
            "method": "POST",
            "header": [],
            "body": {
              "mode": "raw",
              "raw": "{\n    \"email\": \"test@example.com\",\n    \"password\": \"testpass123\"\n}",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            },
            "url": {
              "raw": "{{base_url}}/api/auth/login/",
              "host": [
                "{{base_url}}"
              ],
              "path": [
                "api",
                "auth",
                "login",
                ""
              ]
            }
          },
          "response": []
        }
      ]
    },
    {
      "name": "Funds",
      "item": [
        {
          "name": "Get Fund Houses",
          "request": {
            "method": "GET",
            "header": [
              {
                "key": "Authorization",
                "value": "Token {{auth_token}}"
              }
            ],
            "url": {
              "raw": "{{base_url}}/api/fund-houses/",
              "host": [
                "{{base_url}}"
              ],
              "path": [
                "api",
                "fund-houses",
                ""
              ]
            }
          },
          "response": []
        },
        {
          "name": "Get Mutual Funds",
          "request": {
            "method": "GET",
            "header": [
              {
                "key": "Authorization",
                "value": "Token {{auth_token}}"
              }
            ],
            "url": {
              "raw": "{{base_url}}/api/mutual-funds/?fund_house=1",
              "host": [
                "{{base_url}}"
              ],
              "path": [
                "api",
                "mutual-funds",
                ""
              ],
              "query": [
                {
                  "key": "fund_house",
                  "value": "1"
                }
              ]
            }
          },
          "response": []
        },
        {
          "name": "Portfolio Operations",
          "item": [
            {
              "name": "Create Portfolio Item",
              "request": {
                "method": "POST",
                "header": [
                  {
                    "key": "Authorization",
                    "value": "Token {{auth_token}}"
                  }
                ],
                "body": {
                  "mode": "raw",
                  "raw": "{\n    \"mutual_fund\": 1,\n    \"units\": 10,\n    \"purchase_nav\": 100.50\n}",
                  "options": {
                    "raw": {
                      "language": "json"
                    }
                  }
                },
                "url": {
                  "raw": "{{base_url}}/api/portfolio/",
                  "host": [
                    "{{base_url}}"
                  ],
                  "path": [
                    "api",
                    "portfolio",
                    ""
                  ]
                }
              },
              "response": []
            },
            {
              "name": "List Portfolio",
              "request": {
                "method": "GET",
                "header": [
                  {
                    "key": "Authorization",
                    "value": "Token {{auth_token}}"
                  }
                ],
                "url": {
                  "raw": "{{base_url}}/api/portfolio/",
                  "host": [
                    "{{base_url}}"
                  ],
                  "path": [
                    "api",
                    "portfolio",
                    ""
                  ]
                }
              },
              "response": []
            },
            {
              "name": "Update Portfolio Item",
              "request": {
                "method": "PATCH",
                "header": [
                  {
                    "key": "Authorization",
                    "value": "Token {{auth_token}}"
                  }
                ],
                "body": {
                  "mode": "raw",
                  "raw": "{\n    \"units\": 15\n}",
                  "options": {
                    "raw": {
                      "language": "json"
                    }
                  }
                },
                "url": {
                  "raw": "{{base_url}}/api/portfolio/1/",
                  "host": [
                    "{{base_url}}"
                  ],
                  "path": [
                    "api",
                    "portfolio",
                    "1",
                    ""
                  ]
                }
              },
              "response": []
            },
            {
              "name": "Delete Portfolio Item",
              "request": {
                "method": "DELETE",
                "header": [
                  {
                    "key": "Authorization",
                    "value": "Token {{auth_token}}"
                  }
                ],
                "url": {
                  "raw": "{{base_url}}/api/portfolio/1/",
                  "host": [
                    "{{base_url}}"
                  ],
                  "path": [
                    "api",
                    "portfolio",
                    "1",
                    ""
                  ]
                }
              },
              "response": []
            }
          ]
        }
      ]
    }
  ],
  "variable": [
    {
      "key": "base_url",
      "value": "http://localhost:8000"
    },
    {
      "key": "auth_token",
      "value": ""
    }
  ]
}
   
