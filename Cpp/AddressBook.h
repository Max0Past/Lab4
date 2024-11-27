#pragma once
#ifndef ADDRESSBOOK_H
#define ADDRESSBOOK_H

#include <vector>
#include <memory>
#include <string>
#include "Address.h"
#include "Appartment.h"
#include "PrivateHouse.h"

class UI; // Пряме оголошення для уникнення циклічного включення

class AddressBook {
public:

    AddressBook();

    void AddAddress(shared_ptr<Address> address);
    void AnalyzeAddresses();
    void DisplayAddresses() const;
    void SelectAddressesForMailing();
    void ClearAddresses();
    friend UI;

private:
    vector<shared_ptr<Address>> addresses;
    vector<int> selectedIndices;
};

#endif // ADDRESSBOOK_H
