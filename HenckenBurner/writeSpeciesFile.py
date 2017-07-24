# 07-24-17 

# Description:
# Function to write out files for reactive flows in openfoam.

def writeFile(name, massFrac):
    header = \
"""/*--------------------------------*- C++ -*----------------------------------*\\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  4.1                                   |
|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |
|    \\/     M anipulation  |                                                 |
\\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       volScalarField;
    location    "0.0";
    object      """ + name + \
""";
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 0 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    Coal_in
    {
        type            fixedValue;
        value           uniform 0.0;
    }
    Coflow_in
    {
        type            fixedValue;
        value           uniform """\
+ str(massFrac) + """;
    }
    Inert_in
    {
        type            fixedValue;
        value           uniform 0.0;
    }
    Outlet
    {
        type            zeroGradient;
    }
    Outside
    {
        type            zeroGradient;
    }
    cyclic_neg
    {
        type            cyclic;
    }
    cyclic_pos
    {
        type            cyclic;
    }
}


// ************************************************************************* //"""

    fp = open('openFoam/' + name, "w+")
    fp.writelines(header)
