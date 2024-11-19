{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNv1HT9DgoEukKyq+g0sBuA",
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
        "<a href=\"https://colab.research.google.com/github/luckydogIsaac/2024_phyton_h2/blob/main/hw2-1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DnqPPZ3HPui_",
        "outputId": "1f3e0d9c-a71c-441e-8290-ebc9c9853ec9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "請輸入圓的半徑: 3\n",
            "圓的面積是: 28.26\n",
            "圓的周長是: 18.84\n"
          ]
        }
      ],
      "source": [
        "import math\n",
        "r = float(input(\"請輸入圓的半徑: \"))\n",
        "if r >= 0:\n",
        "    area = r * r * 3.14\n",
        "    circumference = r * 2 * 3.14\n",
        "    print(f\"圓的面積是: {area}\")\n",
        "    print(f\"圓的周長是: {circumference}\")\n",
        "else:\n",
        "    print(\"半徑不能是負數，請輸入一個非負的半徑。\")"
      ]
    }
  ]
}