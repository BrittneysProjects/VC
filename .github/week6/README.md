{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMqukz487x5k03RvpCxIKo4",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/BrittneysProjects/VC/blob/main/Week_6.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install dask[dataframe]\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pm5RLEodIWFF",
        "outputId": "aa0cb8ec-38e6-4ab2-a461-f48e1b8f2313"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: dask[dataframe] in /usr/local/lib/python3.10/dist-packages (2024.7.1)\n",
            "Requirement already satisfied: click>=8.1 in /usr/local/lib/python3.10/dist-packages (from dask[dataframe]) (8.1.7)\n",
            "Requirement already satisfied: cloudpickle>=1.5.0 in /usr/local/lib/python3.10/dist-packages (from dask[dataframe]) (2.2.1)\n",
            "Requirement already satisfied: fsspec>=2021.09.0 in /usr/local/lib/python3.10/dist-packages (from dask[dataframe]) (2024.6.1)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from dask[dataframe]) (24.1)\n",
            "Requirement already satisfied: partd>=1.4.0 in /usr/local/lib/python3.10/dist-packages (from dask[dataframe]) (1.4.2)\n",
            "Requirement already satisfied: pyyaml>=5.3.1 in /usr/local/lib/python3.10/dist-packages (from dask[dataframe]) (6.0.2)\n",
            "Requirement already satisfied: toolz>=0.10.0 in /usr/local/lib/python3.10/dist-packages (from dask[dataframe]) (0.12.1)\n",
            "Requirement already satisfied: importlib-metadata>=4.13.0 in /usr/local/lib/python3.10/dist-packages (from dask[dataframe]) (8.4.0)\n",
            "Requirement already satisfied: pandas>=2.0 in /usr/local/lib/python3.10/dist-packages (from dask[dataframe]) (2.1.4)\n",
            "Requirement already satisfied: dask-expr<1.2,>=1.1 in /usr/local/lib/python3.10/dist-packages (from dask[dataframe]) (1.1.9)\n",
            "Requirement already satisfied: pyarrow>=7.0.0 in /usr/local/lib/python3.10/dist-packages (from dask-expr<1.2,>=1.1->dask[dataframe]) (14.0.2)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata>=4.13.0->dask[dataframe]) (3.20.1)\n",
            "Requirement already satisfied: numpy<2,>=1.22.4 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0->dask[dataframe]) (1.26.4)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0->dask[dataframe]) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0->dask[dataframe]) (2024.1)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=2.0->dask[dataframe]) (2024.1)\n",
            "Requirement already satisfied: locket in /usr/local/lib/python3.10/dist-packages (from partd>=1.4.0->dask[dataframe]) (1.0.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas>=2.0->dask[dataframe]) (1.16.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import dask.dataframe as dd\n",
        "import yaml\n",
        "import os\n",
        "import time\n"
      ],
      "metadata": {
        "id": "TP0S5LJiIY7I"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "uploaded = files.upload()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "UMHFuv9mJJbw",
        "outputId": "9bf216b9-06c6-4d3e-9fac-1c91ecd87f4e"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-a19e2346-a9cf-4f22-92dd-6749f1511ea5\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-a19e2346-a9cf-4f22-92dd-6749f1511ea5\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving turnover.csv to turnover.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TmChjK31JYK_",
        "outputId": "ad3849b0-51d9-402e-edbb-608cdad391cc"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "sample_data  turnover.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "    df_pandas = pd.read_csv('turnover.csv', encoding='utf-8')\n",
        "except UnicodeDecodeError:\n",
        "    try:\n",
        "        df_pandas = pd.read_csv('turnover.csv', encoding='ISO-8859-1')  # Latin1\n",
        "    except UnicodeDecodeError:\n",
        "        df_pandas = pd.read_csv('turnover.csv', encoding='cp1252')  # Another common encoding\n"
      ],
      "metadata": {
        "id": "kjSI2XD9Juki"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install chardet\n",
        "\n",
        "import chardet\n",
        "\n",
        "# Check the first few thousand bytes to guess the encoding\n",
        "with open('turnover.csv', 'rb') as rawdata:\n",
        "    result = chardet.detect(rawdata.read(10000))\n",
        "\n",
        "print(result['encoding'])\n",
        "\n",
        "# Use the detected encoding to read the CSV\n",
        "df_pandas = pd.read_csv('turnover.csv', encoding=result['encoding'])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LtEXdwvPJv9r",
        "outputId": "e6d7a94a-b550-4bff-80d5-ea96a9a0255e"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: chardet in /usr/local/lib/python3.10/dist-packages (5.2.0)\n",
            "ISO-8859-1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def clean_columns(df):\n",
        "    df.columns = df.columns.str.replace('[^\\w]', '', regex=True).str.strip()\n",
        "    return df\n",
        "\n",
        "df_pandas = clean_columns(df_pandas)\n"
      ],
      "metadata": {
        "id": "Zm1alYNYJzge"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import yaml\n",
        "\n",
        "data_schema = {\n",
        "    'separator': ',',\n",
        "    'columns': list(df_pandas.columns)\n",
        "}\n",
        "\n",
        "with open('data_schema.yaml', 'w') as file:\n",
        "    yaml.dump(data_schema, file)\n"
      ],
      "metadata": {
        "id": "kHQJtxGzJ7ND"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "with open('data_schema.yaml', 'r') as file:\n",
        "    schema = yaml.safe_load(file)\n",
        "\n",
        "assert len(df_pandas.columns) == len(schema['columns']), \"Column count mismatch\"\n",
        "assert all(df_pandas.columns == schema['columns']), \"Column names do not match\"\n"
      ],
      "metadata": {
        "id": "zKrMiMmQKApm"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_pandas.to_csv('cleaned_turnover.gz', sep='|', index=False, compression='gzip')\n"
      ],
      "metadata": {
        "id": "Z8OGiGA5KD9W"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "summary = {\n",
        "    'Total Rows': len(df_pandas),\n",
        "    'Total Columns': len(df_pandas.columns),\n",
        "    'File Size': os.path.getsize('cleaned_turnover.gz')  # This returns the file size in bytes\n",
        "}\n",
        "\n",
        "print(summary)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MakgKzusKIRM",
        "outputId": "8b098b46-b8cc-4ffd-9c46-43d5cd106eb4"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'Total Rows': 1129, 'Total Columns': 16, 'File Size': 16921}\n"
          ]
        }
      ]
    }
  ]
}
